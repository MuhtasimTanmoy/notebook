# Serialization

- JSON
    - JSON is textual, its integers and floats can be slow to encode and decode. JSON is not designed for numbers. Also, Comparing strings in JSON can be slow.
- BSON
    - Primary data representation for mongodb.
- MessagePack
    - IDL ( Interface Definition Language )
    - MessagePack supports streaming deserializers. 
    - This feature is useful for network communication.
- Protocol Buffer
    - Protocol Buffers (a.k.a., protobuf) are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.    
- XML
- CSV
- YAML

## Marshalling vs Serialization

Marshaling and serialization are loosely synonymous in the context of remote procedure call, but semantically different as a matter of intent.

- Marshaling is about getting parameters from here to there

- Serialization is about copying structured data to or from a primitive form such as a byte stream. In this sense, serialization is one means to perform marshaling, usually implementing pass-by-value semantics.

- It is also possible for an object to be marshaled by reference, in which case the data "on the wire" is simply location information for the original object. However, such an object may still be amenable to value serialization.

- Marshalling
    - To "marshal" an object means to record its state and codebase(s) in such a way that when the marshalled object is "unmarshalled", a copy of the original object is obtained.

- Serialization
    - To "serialize" an object means to convert its state into a byte stream in such a way that the byte stream can be converted back into a copy of the object.

- Which one to choose?
    - Some environments can have very fast serialization and deserialization to/from msgpack/protobuf's, others not so much. 
    - In general, the more low-level the language/environment the better binary serialization will work. And higher level languages (node.js, .Net, JVM) you will often see that JSON serialization is actually faster. 
    - The question then becomes is your network overhead more or less constrained than your memory/cpu.
    - With regards to msgpack vs bson vs protocol buffers. msgpack is the least bytes of the group, protocol buffers being about the same. 
    - BSON defines more broad native types than the other two, and may be a better match to your object mode, but this makes it more verbose. 
    - Protocol buffers have the advantage of being designed to stream, which makes it a more natural format for a binary transfer/storage format.