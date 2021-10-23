function validateForm() {
    let text;
    let startDate = document.forms["searchForm"]["From"].value;
    let endDate = document.forms["searchForm"]["End"].value;
    let Dstart = new Date(startDate);
    let Dend = new Date(endDate);

    if (Dstart > Dend) {
      console.log("date");
      text = "開始日期不可以比結束日期還要晚";
      document.getElementById("demo").innerHTML = text;
      demo = document.getElementById("demo");
      demo.innerHTML = text;
      demo.style.color = "#dc3545";
      return false;
    } else {
        console.log("驗證成功");
    } 
}
