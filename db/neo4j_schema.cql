CREATE CONSTRAINT ON (u:User) ASSERT u.id IS UNIQUE;
CREATE CONSTRAINT ON (c:Campaign) ASSERT c.id IS UNIQUE;

MATCH (u:User {id:'u1'}), (c:Campaign {id:'c1'})
MERGE (u)-[:ENGAGED]->(c);
