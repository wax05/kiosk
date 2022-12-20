const btn = window.document.getElementById("login");

function client2server(url,data){
    axios.post(url,data)
        .then((response)=>{
            return response
        })
        .catch(function(error){
            console.log(error);
            return error
        });
}

btn.addEventListener("click",()=>{
    let id = document.getElementById("user_id").value;
    let pw = document.getElementById("password").value;
    console.log(id,pw);
    console.log(client2server("/login",{"ID":id,"PW":pw}));
})