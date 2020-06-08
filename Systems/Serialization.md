# Serialization
- JSON
- BSON
    - Primary data representation for mongodb
- MessagePack
    - IDL (Interface Definition Language)
    - MessagePack supports streaming deserializers. This feature is useful for network communication
 - Protocol Buffer
    - Protocol Buffers (a.k.a., protobuf) are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.    


### Which one to choose?
- Some environments can have very fast serialization and deserialization to/from msgpack/protobuf's, others not so much. In general, the more low-level the language/environment the better binary serialization will work. And higher level languages (node.js, .Net, JVM) you will often see that JSON serialization is actually faster. The question then becomes is your network overhead more or less constrained than your memory/cpu.
- With regards to msgpack vs bson vs protocol buffers. msgpack is the least bytes of the group, protocol buffers being about the same. BSON defines more broad native types than the other two, and may be a better match to your object mode, but this makes it more verbose. Protocol buffers have the advantage of being designed to stream, which makes it a more natural format for a binary transfer/storage format.
