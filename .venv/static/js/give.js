$(document).ready(async () => {
    res = null
    err = null
    await axios.post("/get/code")
        .then((response) => {
            res = response
        })
        .catch((error)=>{
            err = error
        });
    console.log(res)
    if (res["data"]["status"] !== true) {
        alert(res["data"]["error"])
    }
    let title = document.getElementById("CodeShow");
    title.innerHTML = res["data"]["Code"];
});