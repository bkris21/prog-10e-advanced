

let keys = ["id", "username", "email"];
document.querySelector('#getDataBtn').addEventListener("click", startGetUsers);
document.querySelector('#add-new-user').addEventListener("click",addNewUser);
function getServerData(url) {
    let fetchOptions = {
        method: "GET",
        mode: "cors",
        cache: "no-cache"
    };
    return fetch(url, fetchOptions).then(
        response => response.json(),
        err => console.error(err)
    );
}
function startGetUsers() {
    getServerData("http://localhost:5000/users").then(
        data => fillDataTable(data, "userTable")
    );
};

function addNewUser(){
    let nameIn = document.querySelector('#name-input').value;
    let emailIn = document.querySelector('#email-input').value;
    let alert = document.querySelector("#my-alert");
    let fetchOptions = {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({name: nameIn, email: emailIn})
        }
       let response = fetch("http://localhost:5000/users",fetchOptions).then(
            response => response.json()
        )

        response.then(
            data => data["message"]=="ok"?alert.style="display:block":console.log(ERR)
        )
        
        startGetUsers();
    };
    



function fillDataTable(data, tableID) {
    let table = document.querySelector(`#${tableID}`);
    if (!table) {
        console.error(`Table "${tableID}" is not found.`);
        return;
    }

    // Add new user row to the table.
    let tBody = table.querySelector("tbody");
    tBody.innerHTML = '';
    for (let row of data) {
        let tr = createAnyElement("tr");
        for (let k of keys) {
            let td = createAnyElement("td");
            let input = createAnyElement("input", {
                class: "form-control",
                value: row[k],
                name: k,
            });
        
            td.appendChild(input);
            tr.appendChild(td);
        }
        let btnGroup = createBtnGroup();
        tr.appendChild(btnGroup);
        tBody.appendChild(tr);
    }
}
function createAnyElement(name, attributes) {
    let element = document.createElement(name);
    for (let k in attributes) {
        element.setAttribute(k, attributes[k]);
    }
  
    return element;
}

function createBtnGroup() {
    let group = createAnyElement("div", { class: "btn btn-group" });
    let infoBtn = createAnyElement("button", { class: "btn btn-info", onclick: "setRow(this)" });
    infoBtn.innerHTML = '<i class="fa fa-refresh" aria-hidden="true"></i>';
    let delBtn = createAnyElement("button", { class: "btn btn-danger", onclick: "delRow(this)" });
    delBtn.innerHTML = '<i class="fa fa-trash-o" aria-hidden="true"></i>';

    group.appendChild(infoBtn);
    group.appendChild(delBtn);

    let td = createAnyElement("td");
    td.appendChild(group);
    return td;
}


