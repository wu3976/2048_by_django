rep = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]];

/**
 * Get the id from the given 2-ele array pos
 * @param pos An 2-ele array
 * @returns {string}
 */
const getIdFromPos = (pos) => {
    return pos[0] + "_" + pos[1];
}

/**
 *
 * @param pos An 2 element array, [row, col], representing the target.
 * @param status Representing the model status of the target. 0 -> empty, other -> 2^status
 */
const updateView = (pos, status) => {
    let id = getIdFromPos(pos);
    let obj = document.getElementById(id);
    if (status === 0){
        obj.innerText = "";
    } else {
        obj.innerText = Math.pow(2, status).toString();
    }
}

/**
 * @return {boolean} Whether the game is over
 */
const gameover = () => {
    let result = true;
    for (let i = 0; i < rep.length && result; i++){
        for (let j = 0; j < rep[i].length && result; j++){
            if (rep[i][j] === 0){
                result = false;
            }
        }
    }
    return result;
}

const hasNext = (ori) => {
    if (ori[0] === "h"){
        for (let line of rep){
            for (let i = 0; i < line.length; i++){
                for (let j = 1; j < line.length; j++){
                    // TODO: xxx
                }
            }
        }
    } else if (ori[0] === "v"){
        // TODO: xxx
    }
}