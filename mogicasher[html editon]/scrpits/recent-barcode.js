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
}
