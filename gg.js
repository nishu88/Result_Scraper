function func()
{   
    
    
    var x=document.getElementById('year').value;
    var y=document.getElementById('branch').value;
    var z=document.getElementById('usnnum').value;
    var usn="1RV"+x+y+z;
    //alert(usn);
    
    ff="ECE/Semester 6"
    var ref=firebase.database().ref(ff);
    ref.on('value',g,e);
    
    function g(data){
        d=data.val();
        var a1=d[usn]['NAME'];
        var a2=d[usn]['sgpa'];
        var a3=d[usn]['COMMUNICATION SYSTEM II'];
        var a4=d[usn]['COMPUTER COMMUNICATION NETWORKS'];
        var a5=d[usn]['ANALOG AND MIXED SIGNAL IC DESIGN'];        
        var a6=d[usn]['ELECTIVE C'];
        var a7=d[usn]['ELECTIVE D'];
        var a8=d[usn]['ELECTIVE E'];
        var a9=d[usn]['FOUNDATIONS OF MANAGEMENT AND ECONOMICS'];
        var a10=d[usn]['PROFESSIONAL PRACTICE III'];
        alert(a1+a2+a3+a4+a5+a6+a7+a8+a9+a10)
        
        
        
    }
    function e(err)
    {}
    
}