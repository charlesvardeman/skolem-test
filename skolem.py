from rdflib import Graph, Namespace, URIRef

GEOSCHEMAS = Namespace("http://ld.geoschemas.org")

if __name__ == '__main__':
    g = Graph()
    g.parse("./report.ttl", format="ttl")

    skolemver = g.skolemize(authority="http://ld.geoschemas.org")
    print(skolemver.serialize(format="xml").decode('utf-8'))

