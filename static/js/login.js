const btn = window.document.getElementById("login");

/**
 * Clear User input
 */
function ClearUserInput() {
    let UserIDInput = document.getElementById("user_id");
    let UserPWInput = document.getElementById("password");
    UserIDInput.value = null;
    UserPWInput.value = null;
}

btn.addEventListener("click",async ()=>{
    let id = document.getElementById("user_id").value;
    let pw = document.getElementById("password").value;
    ServerResponse = null;
    await axios.post("/login",{"ID":id, "PW":pw})
        .then((response) => {
            ServerResponse = response;
        })
        .catch((error) => {
            console.log(error);
        });
    if (ServerResponse["status"] != 200) {
        console.log(`ServerResponse: ${ServerResponse["status"]}`);
    } else {
        if (ServerResponse["data"]["status"]) {
            window.location.href = "/admin"
        } else {
            switch(ServerResponse["data"]["error"]) {
                case "ID or PW not Match":
                    alert("아이디 혹은 비밀번호가 맞지 않습니다");
                    ClearUserInput()
                    break;
                case "BlockWord":
                    alert("ID에 금지된 단어가 들어있습니다");
                    ClearUserInput()
                    break;
                default:
                    alert("확인되지 않은 에러타입입니다 관리자에게 말해주세요");
                    ClearUserInput()
                    break;
            }
        }
    }
})