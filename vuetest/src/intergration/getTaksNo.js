function getTaskNo() {
    function addZero(num) {
        if (num >= 0 && num < 10) {
            num = 0 + String(num)
            return num
        } else
            return String(num)
    }

    const date = new Date();

    const timeStamp = date.getFullYear() + addZero(date.getMonth() + 1) + addZero(date.getDate()) +
        addZero(date.getHours()) + addZero(date.getMinutes()) + addZero(date.getSeconds()) +
        Math.floor(Math.random() * (9999 - 1000) + 1000);
    return timeStamp
}

export {getTaskNo}