from myaiplatform.config import VECTOR_DB

if VECTOR_DB == "milvus":
    from myaiplatform.retrieval.vector.dbs.milvus import MilvusClient

    VECTOR_DB_CLIENT = MilvusClient()
elif VECTOR_DB == "qdrant":
    from myaiplatform.retrieval.vector.dbs.qdrant import QdrantClient

    VECTOR_DB_CLIENT = QdrantClient()
elif VECTOR_DB == "opensearch":
    from myaiplatform.retrieval.vector.dbs.opensearch import OpenSearchClient

    VECTOR_DB_CLIENT = OpenSearchClient()
elif VECTOR_DB == "pgvector":
    from myaiplatform.retrieval.vector.dbs.pgvector import PgvectorClient

    VECTOR_DB_CLIENT = PgvectorClient()
elif VECTOR_DB == "elasticsearch":
    from myaiplatform.retrieval.vector.dbs.elasticsearch import ElasticsearchClient

    VECTOR_DB_CLIENT = ElasticsearchClient()
elif VECTOR_DB == "pinecone":
    from myaiplatform.retrieval.vector.dbs.pinecone import PineconeClient

    VECTOR_DB_CLIENT = PineconeClient()
else:
    from myaiplatform.retrieval.vector.dbs.chroma import ChromaClient

    VECTOR_DB_CLIENT = ChromaClient()
