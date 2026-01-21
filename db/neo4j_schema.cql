/* neo4j_schema.cql - example graph constraints */
CREATE CONSTRAINT conversation_id_unique IF NOT EXISTS
FOR (c:Conversation) REQUIRE c.id IS UNIQUE;
