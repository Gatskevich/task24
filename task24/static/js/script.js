let counter = 1;
function addForm(){

    parent = document.getElementById('form-input')
    let input = document.createElement('input'),
        label = document.createElement('label');

    input.name = 'name' + counter;
    input.id = counter;
    label.innerHTML = "name" + counter++ + ":";

    parent.appendChild(label);
    parent.appendChild(input);
}