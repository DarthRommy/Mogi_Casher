/**---- 入力欄周り ----*/
function display_recent(){
    const recent = document.getElementById("recent-barcode");
    const value = document.getElementById("inputBarcode").value;

    const space = value.includes(" ")
    console.log(value, space)

    if (value == ""){
        $(".error-no-input").modal()
    }else if (space == true){
        $(".error-unex-input").modal()
    }else{
        recent.textContent = value;
    }
    document.getElementById("inputBarcode").value = "";
};
/**----そのままEnterを押すとなぜかリロードが入るのでイベントとして処理---- */
window.document.onkeydown = function(event){
    if (event.key === "Enter") {
        display_recent()
    }
};

/**---- 発団名入力欄 ----*/
function storeName() {
    $(".storeName").modal();
};

function clearStoreName() {
    document.getElementById("inputStoreName").value = "";
};

function logChkbox() {
    const value = document.getElementById("chk").checked;
    console.log(value);
};

$(window).on('beforeunload', function(e) {
    return 'ちょっと待ってくださいよ。まだダメですよ。';
});
