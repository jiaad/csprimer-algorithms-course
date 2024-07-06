/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {
    const dag = {}
    for(let i = 0; i < graph.length; i++){
        dag[i] = [...graph[i]]
    }
    /**
    * bfs
    * q = [[start, [start]]]
    * while(q)
    *   let [vrtx, path] = q.shift()
    *   if vrtx === end: res.push(path + vrtx)
    *   for dag[vrtx]:
            add to the q

     */
    let [start, end] = [0, graph.length - 1]
	console.log(start, end)
    let q = [[start, [start]]]
    let [res, visited] = [[], new Set()]
     while(q.length){  
       let [vrtx, path] = q.shift()
	console.log(vrtx, end, vrtx === end)
       if(vrtx === end) {
		res.push(path)
	}
       for(let dvrtx of dag[vrtx]){
	    visited.add(dvrtx)
			
            q.push([dvrtx, path.concat(dvrtx)])
       } 
     }
     return res
};

console.log(allPathsSourceTarget([[1,2],[3],[3],[]]))
