$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    // Siriwave configuration
    var javiahs_speaking = new SiriWave({
        container: document.getElementById("siriwave-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });

    // Javiah's message animation via siriwave
    $('.javiahs-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // mic button click event

    $("#MicBtn").click(function () {
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#javiahs_speaking").attr("hidden", false);
        eel.allCommands()()
    });


    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#javiahs_speaking").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // to play assisatnt 
    function PlayAssistant(message) {

        if (message != "") {

            $("#Oval").attr("hidden", true);
            $("#javiahs_speaking").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }

    }

    // toogle fucntion to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // key up event handler on text box
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)

    });

    // send button event handler
    $("#SendBtn").click(function () {

        let message = $("#chatbox").val()
        PlayAssistant(message)

    });


    // enter press event handler on chat box
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });

    // eel.expose(receiverText);
    // function receiverText(message) {
    //     $('#chat-canvas-body').append('<div class="message received">' + message + '</div>');
    //     // Scroll to bottom of chat canvas
    //     $('#chat-canvas-body').scrollTop($('#chat-canvas-body')[0].scrollHeight);
    // }

    // eel.expose(senderText);
    // function senderText(message) {
    //     $('#chat-canvas-body').append('<div class="message sent">' + message + '</div>');
    //     // Scroll to bottom of chat canvas
    //     $('#chat-canvas-body').scrollTop($('#chat-canvas-body')[0].scrollHeight);
    // }

    // // Define a function to display a message
    // eel.expose(DisplayMessage);
    // function DisplayMessage(message) {
    //     // Append the message to the chat canvas body
    //     $('#chat-canvas-body').append('<div class="message">' + message + '</div>');
    //     // Scroll to bottom of the chat canvas body
    //     $('#chat-canvas-body').scrollTop($('#chat-canvas-body')[0].scrollHeight);
    // }

});