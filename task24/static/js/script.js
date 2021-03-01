let counter = 1;
function addForm(){
    parent = document.getElementById('form-input')
    let input = document.createElement('input'),
        label = document.createElement('label');

    input.name = 'name' + counter;
    label.innerHTML = "name" + counter++ + ":";

    parent.appendChild(label);
    parent.appendChild(input);
    return counter
}