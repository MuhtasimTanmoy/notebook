# AMQP

### Message Format
- The headers and properties of the message are basically key/value pairs. 
- The difference between them is that headers are defined by the AMQP specification whereas properties can contain arbitrary, application-specific information. 
- The actual message content is just a sequence of bytes, so if you want to pass text around in your messages, then you should standardize on an encoding. 
- UTF-8 is a good bet. You can specify a content type and encoding in the message headers if you want, but that's apparently not particularly common.