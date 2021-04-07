# Tokio

Tokio is an asyncronous runtime for rust programming language.

```rust

async fn print() {
    time::sleep(Duration::from_millis(10)).await;
    println!("Done sleeping");
}

// await part is divide into two poritons

enum Task {
    Init,
    AwaitSleep(sleep),
}

```

How it works under the hood?
- The compiler turns asyncrounous task into state machine.
- Java program cant have segfault but can have data reces.
- ARC gives smart pointer. Mutex lock provides another smart pointer. When it goes out of scope it is unlocked autometically.
- MutexLockGuard is a smart pointer.
    - Gives multiple reference to the data inside.

```rust


struct Database(Arc <Mutex <HashMap <String,Byte> > >)

#[tokio::main]
async fn main() -> io::Result<()> {
    let listener = TcpListener::bind("localhost:8000").await?;
    let database = Database::new()
    loop {
        // let {mut socket, _ } = listener.accept().await?;
        let {conn, _} = listener.accept().await?;

        let db = database.clone();

        tokio::spawn( async move {
            let cmd = conn.recv_frame().await?;

            let response = cmd.apply(&db);

            socket.write_frame(&response).await?;

            // socket.write_all(b"Hello world").await
        });
    }
} 


fn get(db: &Db, key: String) -> Frame {
    // Lock the db while we use it
    let locked = db.lock();

    if let Some(value) = locked.find(key) {
        Frame::bulk(value)
    } else {
        Frame::Null
    }
}

fn put(db: &Db, key: String, value: Byte) -> Frame {
    let locked = db.lock();

    locked.insert(key, value);

    Frame::Simple("Ok")
}

// epoll provides io events
// kqueue bsd
// iopc windows

```

# Reference
- [AWS re:Invent 2020: Next-gen networking infrastructure with Rust and Tokio ](https://www.youtube.com/watch?v=MZyleK8elPk&ab_channel=AWSEvents)