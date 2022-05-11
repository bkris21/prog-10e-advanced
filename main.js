
document.querySelector("#getDataBtn").addEventListener("click", startGetUsers)
document.querySelector("#add-user-btn").addEventListener("click", addNewUser)

function getServerData(url){
    let fetchOptions = {
        method: "GET",
        mode: "cors"
    };

    return fetch(url, fetchOptions)
        .then(response => response.json(),
              err => console.log(err))
}

function startGetUsers(){
    getServerData("http://localhost:5000/users")
        .then(data => fillDataTable(data));
}

function fillDataTable(data){
    let keys = ["id","username","email"]

    let table = document.querySelector("#userTable");
    console.log(table);
    let tBody = table.querySelector("tbody");
    tBody.innerHTML =''
    for(let row of data){
        let tr = document.createElement("tr");
        for(let k of keys){
            let td = document.createElement("td");
            let input = document.createElement("input");
            input.setAttribute("class", "form-control");
            input.setAttribute("value", row[k])

            td.appendChild(input);
            tr.appendChild(td);
        };
        tBody.appendChild(tr);
    }
    

}


function addNewUser(){
    let nameIn = document.querySelector("#user-input").value;
    let emailIn = document.querySelector("#email-input").value;

    let fetchOptions = {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        headers:{
            'Accept':'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({name:nameIn,email:emailIn})
    }

    let response = fetch("http://localhost:5000/users",fetchOptions).then(
        response=>response.json()
    );

    startGetUsers();
}