import React, {useEffect, useRef, useState} from 'react';
import {socketService} from "../services/socketService";

const ChatComponent = () => {
    const [room, setRoom] = useState(null)

    const [socketClient, setSocketClient] = useState(null)

    const [message, setMessage] = useState([])

    const roomInput = useRef()

    useEffect(() => {
        if (room){
            socketInit(room).then(client=> setSocketClient(client))
        }
    }, [room]);

    const socketInit = async (room)=>{
        const {chat} = await socketService()
        const client = await chat(room)

        client.onopen = ()=>{
            console.log('Chat socket connected');
        }

        client.onmessage = ({data}) =>{
            const {message,user} = JSON.parse(data.toString())
            setMessage(prevState => [...prevState, {user, message}])
        }

        return client
    }

    const roomHandler = ()=>{
        setRoom(roomInput.current.value)
    }

    const handleEnterKey = (e)=>{
        if (e.key === 'Enter'){
            socketClient.send(JSON.stringify(
                {data:e.target.value,
                        action: 'send_message',
                    request_id: new Date().getTime()
                }
            ))
            e.target.value = ''
        }

    }

    return (
        <div>
            {
                !room?
                    <div>
                        <input type="text" ref={roomInput} />
                        <button onClick={roomHandler}>Enter Room</button>
                    </div>
                    :
                    <div>
                        {
                            message.map(message=><div>{message.user}: {message.message}</div>)

                        }
                        <input type="text" onKeyDown={handleEnterKey} />
                    </div>
            }
        </div>
    );
};

export default ChatComponent;