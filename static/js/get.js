let GetTrue = false;
const Btn = document.getElementById("btn");

function ClearUserInput() {
    let ClearCodeInput = document.getElementById("code");
    ClearCodeInput.value = null;
}

Btn.addEventListener("click", async ()=>{
    let CodeInput = document.getElementById("code").value;
    let UserName = document.getElementById("get").value;
    let ServerResponse = null;
    await axios.post("/get",{"Code":CodeInput,"Name":UserName})
        .then((response) => {
            ServerResponse = response;
        })
        .catch((error) => {
            console.log(error);
        });
    if (ServerResponse !== null && ServerResponse["status"] === 200) { //Server Response 200
        if (ServerResponse["data"]["status"] === true) {
            GetTrue = true;
            alert("상품수령이 완료 되었습니다");
            location.href = "/get/check";
        } else {
            switch (ServerResponse["data"]["error"]) {
                case "SQL Error":
                    alert("SQL ERROR");
                    ClearUserInput();
                    break;
                case "Block WardError":
                    alert("금지어가 포함되어있습니다(-,#,*,/)");
                    ClearUserInput();
                    break;
                case "UsedCode":
                    alert("이미 사용된 코드입니다");
                    ClearUserInput();
                    break;
                case "No Code":
                    alert("등록된 코드가 없습니다.다시 확인해주세요");
                    ClearUserInput();
                    break;
            }
        }
    } else if (ServerResponse["status"] >= 500) {//Server Response 500
        alert("서버측 오류입니다 관리자에게 말해주세요");
    } else {//Other SererResponse Error
        alert(`오류가 발생했습니다 HTTP Status : ${ServerResponse["status"]}`);
    }
});