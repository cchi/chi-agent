from llama_index import SimpleDirectoryReader, VectorStoreIndex


def main():
    reader = SimpleDirectoryReader("data")
    docs = reader.load_data()
    index = VectorStoreIndex.from_documents(docs)
    index.storage_context.persist(persist_dir="index")
    print("Index built and saved to ./index")


if __name__ == "__main__":
    main()
