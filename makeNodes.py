from py2neo import Graph, Path, Node, Relationship, authenticate

authenticate("localhost:7474", "neo4j", "research");
graph = Graph("http://localhost:7474/db/data");

Content = ['Animals also need water to survive. Water is used to break down and move materials throughout the body.', 'Animals cannot make their own food so they must eat to get nutrients. Nutrients are necessary for growth and energy.'];
Keywords = [[],['nutrients']];

for a,b in zip(Content,Keywords):
	graph.create(Node("Content", Text = a, keywords = b));
content = ['Animals take in air by breathing. They need oxygen,
which is in the air. Oxygen allows the animal to make
and use energy, which it needs to survive.', 'Animals also need water to survive. Water is used to break down and move materials throughout the body.', 'Animals cannot make their own food so they must eat to get nutrients. Nutrients are necessary for growth and energy.'];
keywords = [[],[],['nutrients']];
for a,b in zip(content, keywords)
	graph.create(Relationship(Node("Topic1", name = "Animals"), "CONTAINS", Node("Content", Text=a, keywords=b);


  
