var me = {};

var you = {};


var apigClient = apigClientFactory.newClient()
var CognitoAuth = AmazonCognitoIdentity.CognitoAuth;

var authData = {
  ClientId : '3bhjhvmravrfo08feltv7v640l', // Your client id here
  AppWebDomain : 'https://spm486.auth.us-east-1.amazoncognito.com',
  TokenScopesArray : ['phone', 'email', 'profile','openid', 'aws.cognito.signin.user.admin'], // e.g.['phone', 'email', 'profile','openid', 'aws.cognito.signin.user.admin'],
  RedirectUriSignIn : 'https://s3.amazonaws.com/testlogout/chatbot.html',
  RedirectUriSignOut : 'https://spm486.auth.us-east-1.amazoncognito.com/login?response_type=token&client_id=3bhjhvmravrfo08feltv7v640l&redirect_uri=https://s3.amazonaws.com/testlogout/chatbot.html',
  UserPoolId : 'us-east-1_hzXBMQUup', // Your user pool id here 
};
var auth = new AmazonCognitoIdentity.CognitoAuth(authData);

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}            

//-- No use time. It is a javaScript effect.
function insertChat(who, text, time = 0){
    var control = "";
    var date = formatAMPM(new Date());
    
    if (who == "me"){
        
        control = '<li style="width:100%">' +
                        '<div class="msj macro">' +
                            '<div class="text text-l">' +
                                '<p>'+ text +'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                        '</div>' +
                    '</li>';                    
    }else{
        control = '<li style="width:100%;">' +
                        '<div class="msj-rta macro">' +
                            '<div class="text text-r">' +
                                '<p>'+text+'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                        '<div class="avatar" style="padding:0px 0px 0px 10px !important"></div>' +                                
                  '</li>';
    }
    setTimeout(
        function(){                        
            $("ul").append(control);

        }, time);
    
}

function resetChat(){
    $("ul").empty();
}

$(".mytext").on("keyup", function(e){
    if (e.which == 13){
        var text = $(this).val();
        if (text !== ""){
            insertChat("me", text); 
            format_msg(text);           
            $(this).val('');
        }
    }
});



function format_msg(user_message){
   var body =  {
      "messages" : [
      {
        "type": "string",
        "unstructured": {
          "id": "string",
          "text": user_message,
          "timestamp": "timestamp"
        }
      }
    ]
  }
   console.log("request sent")
   console.log(body)
   chatbotPost(body)  
}

function loadDoc() {
    var url = window.location.href;
    url_Split = url.split("/");
    token_split = url_Split[url_Split.length - 1].split("&");
    id_token = token_split[0].split("=");
    var token_id_final = id_token[1];
    console.log(id_token[1])
    var additionalParams = {
  // If there are any unmodeled query parameters or headers that must be
  //   sent with the request, add them here.
   headers: {
    'Authorization':token_id_final
  }
}
return additionalParams
}

function chatbotPost(body) {
  var bot_reply

  additionalParams = loadDoc()
  apigClient.chatbotPost({},body,additionalParams)
      .then(function(result){
        console.log("Result back")
        console.log(result.data.body)
        bot_reply = result.data.body
        insertChat("bot",bot_reply)
      }).catch( function(result){
        console.log(result)
      });
      
}

document.getElementById("logout").addEventListener("click", myFunction);

function myFunction() {
    console.log("YOU CLICKED ME!");
    auth.signOut();
    window.location.replace("https://spm486.auth.us-east-1.amazoncognito.com/login?response_type=token&client_id=3bhjhvmravrfo08feltv7v640l&redirect_uri=https://s3.amazonaws.com/testlogout/chatbot.html");
}