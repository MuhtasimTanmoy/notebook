# threadpool

- std::function is a type erasure object.
    - ` std::function< double( int, int ) > ` double return type, two int argument
    - `packaged_task` to make future


```c++
template<class T>
struct threadsafe_queue {
  [[nodiscard]] std::optional<T> pop() {
    auto l = lock();
    cv.wait(l, [&]{ return is_aborted() || !data.empty(); });
    if (is_aborted())
      return {};
    auto r = std::move(data.front());
    data.pop_front();
    cv.notify_all(); // for wait_until_empty
    return r; // might need std::move here, depending on compiler version
  }
  bool push(T t) {
    auto l = lock();
    if (is_aborted()) return false;
    data.push_back(std::move(t));
    cv.notify_one();
    return true;
  }
  void set_abort_flag() {
    auto l = lock(); // still need this
    aborted = true;
    data.clear();
    cv.notify_all();
  }
  [[nodiscard]] bool is_aborted() const { return aborted; }
  void wait_until_empty() {
    auto l = lock();
    cv.wait(l, [&]{ return data.empty(); });
  }
private:
  std::unique_lock<std::mutex> lock() {
    return std::unique_lock<std::mutex>(m);
  }
  std::condition_variable cv;
  std::mutex m;
  std::atomic<bool> aborted{false};
  std::deque<T> data;
};






struct threadpool {
  explicit threadpool(std::size_t count)
  {
    for (std::size_t i = 0; i < count; ++i) {
      threads.emplace_back([&]{
        // abort handled by empty pop:
        while( auto f = queue.pop() ) {
          (*f)();
        }
      });
    }
  }
  void set_abort_flag() {
    queue.set_abort_flag();
  }
  [[nodiscard]] bool is_aborted() const {
    return queue.is_aborted();
  }
  ~threadpool() {
    queue.wait_until_empty();
    queue.set_abort_flag(); // get threads to leave the queue
    for (std::thread& t:threads)
      t.join();
  }
  template<class F,
    class R=typename std::result_of<F()>::type
  >
  std::future<R> push_task( F f ) {
    std::packaged_task<R()> task( std::move(f) );
    auto ret = task.get_future();
    if (queue.push( std::packaged_task<void()>(std::move(task)) )) // wait, this works?  Yes it does.
      return ret;
    else
      return {}; // cannot push, already aborted
  }
private:
  // yes, void.  This is evil but it works
  threadsafe_queue<std::packaged_task<void()>> queue;
  std::vector<std::thread> threads;
};
```