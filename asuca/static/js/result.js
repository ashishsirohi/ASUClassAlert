/**
 * Created by ashish on 6/29/17.
 */
function result_status(seats, cid, avl) {
    if(cid == "None"){
        document.getElementById("notify").style.display = "none";
        document.getElementById("reg").style.display = "none";
        document.getElementById("av").style.display = "none";
        document.getElementById("na").style.display = "none";
    }
    else{
        if(avl){
            document.getElementById("notify").style.display = "none";
            document.getElementById("no_cid").style.display = "none";
            document.getElementById("na").style.display = "none";
        }
        else {
            document.getElementById("reg").style.display = "none";
            document.getElementById("no_cid").style.display = "none";
            document.getElementById("av").style.display = "none";
        }
    }
}
