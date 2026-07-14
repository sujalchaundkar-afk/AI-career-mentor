
document.querySelector("form").addEventListener("submit", function(event){

    event.preventDefault();

    var skills = document.querySelectorAll("input")[2].value.toLowerCase();
    var interest = document.querySelectorAll("input")[3].value.toLowerCase();

    var result = "";

    if(skills.includes("python") || interest.includes("ai")){
        result = "Recommended Career: AI / Machine Learning Engineer";
    }
    else if(skills.includes("html") || skills.includes("css")){
        result = "Recommended Career: Frontend Web Developer";
    }
    else if(skills.includes("java")){
        result = "Recommended Career: Java Developer";
    }
    else if(skills.includes("sql")){
        result = "Recommended Career: Database Administrator";
    }
    else{
        result = "Explore different skills to find your best career path.";
    }

    document.getElementById("result").innerHTML = "<h3>" + result + "</h3>";

});
