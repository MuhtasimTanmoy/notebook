# Elastic Search

### Structure

- Elastic Search forms with index
- Index (Logical namespace / DB Name)
    - Divided into Shrads (Types / Table / Schema)
- Each shard has replica
- Each shard is Lucene index
    - For inverted search
- Divided into Segments
    - Inverted index
- Segments are immutable
- Apache Lucene
    - Powerful open-source full-text search library
- DB normalize
    - Case disposal, punctuation
    - Common word remove    
    - Stop word list
    - Lemma
        - Mapping different usage to one
- Tokenization
    - Stemming > Buying > Buy
- After 1 second index refresh happens
    - Doc indexed
- Translog (30 min or 512mb)
- Master node and Data Node available

- Inverted index
    - A document is the unit of data in Elasticsearch and an inverted index is created by tokenizing the terms in the document, creating a sorted list of all unique terms, and associating a list of documents with where the word can be found.
      - Record level inverted index (word -> record)
      - Word level inverted index (word -> record, position )

### Internal Usage
- Porters stemmer algo
    - The Porter stemming algorithm (or ‘Porter stemmer’) is a process for removing the commoner morphological and inflexional endings from words in English. 
    - Its main use is as part of a term normalization process that is usually done when setting up Information Retrieval systems.
- Murmur3 hash function
- Why indexing?
    - Database blocks stored like a linked list
    - For searching  N blocks 
        - when not sorted searching requires `N/2` access avg
        - when duplicates then `N`
        - when sorted `logN`

### Database Indexing

- Creating an index on a field in a table creates another data structure that holds the field value and a pointer to the record it relates to. 

- This index structure is then sorted, allowing Binary Searches to be performed on it.

- Given our sample database of `r = 5,000,000` records of a fixed size giving a record length of `R = 204` bytes and they are stored in a table using the MyISAM engine which is using the default block size B = `1,024` bytes. 

- The blocking factor of the table would be `bfr = (B/R) = 1024/204 = 5` records per disk block.

- The total number of blocks required to hold the table is `N = (r/bfr) = 5000000/5 = 1,000,000` blocks.

- High cardinality
    - Better indexing

- Type of index 
    - Primary index
    - Dense index 
        - All records map to index
    - Sparse index
        - Few records map to sorted index
    - Sparse index is not possible if records are not organized/sorted

- Graph database which considers relation and data 
secondary index

### Notes
- Low cardinality in the database 
    - Common attribute
    - Easy for indexing
- Made efficient through bitmap indexing
- DB Normalization - Denormalization
    - A list of words contained in a document. (Forward index)
    - A list of documents containing a word. (Inverted index)

### References
- [Anatomy of Elastic Search](https://blog.insightdatascience.com/anatomy-of-an-elasticsearch-cluster-part-i-7ac9a13b05db)
- [How does database indexing work?](https://stackoverflow.com/questions/1108/how-does-database-indexing-work)