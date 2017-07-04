/**
 * Created by ashish on 6/27/17.
 */

function login_status(status) {
    //alert(status);
    if(status == 0){
        document.getElementById("ulogout").style.display = "none";
        document.getElementById("mycourses").style.display = "none";
    }
    else{
        document.getElementById("ulogin").style.display = "none";
        document.getElementById("usignup").style.display = "none";
    }
}