import {authService} from "./authService";
import {w3cwebsocket as W3cwebsocket} from 'websocket'

const baseURL = 'ws://localhost/api'
const socketService = async ()=>{
    console.log('::::::6')
    const {data: {token}} = await authService.getSocketToken()
    console.log('::::::8')
    return {
        chat: (room) => new W3cwebsocket(`${baseURL}/chat/${room}/?token=${token}`),
        car: ()=> new  W3cwebsocket(`${baseURL}/cars/?token=${token}`)
    }

}

export {
    socketService
}