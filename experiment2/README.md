ORI mesh 45570 vert.

auto 
- rm duplicate vert 45189
- rm loose geometry 45189
- rm separate mesh  45182

auto 2
- rm duplicate vertices (remove doubles)    45181
- rm zero area faces and zero length edges (degenerate dissolve) -1 vert 16 edges 5 faces   45188
- make all faces convex (split concave faces) no change
- rm all non-manifold vertices and edges    2934/45188 or 42254
- fill in holes using boundary edge loops
- triangulate faces
- rm disconnected vertices and edges (loose geometry) 42187
