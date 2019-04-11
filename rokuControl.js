let roku_ip = "http://192.168.1.10:8060"
const keyMap = {
    "ArrowUp": "up",
    "ArrowDown": "down",
    "ArrowLeft": "left",
    "ArrowRight": "right",
    "Tab": "select",
    "Backquote":"select",
    "Period": "fwd",
    "Comma": "rev",
    "Backspace": "backspace",
    "Enter": "enter",
    "Escape": "back",
}
const allowedToType = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
async function sendKeypress(keyname) {
    let response = await fetch((roku_ip + "/keypress/" + keyname), { method: "post", mode: "no-cors", })
    console.log(response)
}
async function launchApp(appid) {
    let response = await fetch((roku_ip + "/launch/" + appid), { method: "post", mode: "no-cors", })
    console.log(response)
}
function attachKeypress() {
    document.querySelector("body").addEventListener('keydown', handleKey);
}
function disableBinding() {
    document.querySelector("body").removeEventListener('keydown', handleKey);
}
function setIP() {
    roku_ip = document.querySelector("#ip").value;
}

function handleKey(e) {
    console.log(keyMap[e.code])
    if (keyMap[e.code] !== undefined) {
        sendKeypress(keyMap[e.code]);
    } else {
        if (allowedToType.indexOf(e.key) > -1) {
            sendKeypress("lit_" + encodeURI(e.key));
        }
    }
}
