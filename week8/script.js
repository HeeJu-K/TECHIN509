let buttons = document.querySelectorAll(".board-button");
let i = 0;
// var buttons = document.getElementsByTagName('boardBotton');
// for (let i = 0; i < buttons.length; i++) {
//     let button = buttons[i];
//     button.addEventListener('click', function handleClick() {
//         if (i%2 == 0) 
//             button.textContent = 'X';
//         else
//             button.textContent = 'O';
//         i++
//     });
//     // ...
// }
buttons.forEach((button) => {

    button.addEventListener("click", () => {
        console.log("here" , i)
        if (i%2 == 0) { 
            button.innerText = 'X';
        }
        else { 
            button.innerText = 'O';
        }
        i++;
    });
})

