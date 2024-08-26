import React, {useEffect, useState} from 'react';
import {carService} from "../services/carService";
import CarComponent from "./CarComponent";
import {socketService} from "../services/socketService";

const CarsComponent = () => {
    const [cars, setCars] = useState([])
    const [trigger, setTrigger] = useState(null)

    useEffect(() => {
        carService.getAll().then(({data})=>setCars(data))
    }, [trigger]);

    useEffect(() => {
        console.log('::::15')
        socketInit().then()
    }, []);

    const socketInit = async ()=>{
        console.log('::::20')
        const {car} = await socketService()
        const client = await car()
        console.log('::::23')
        client.onopen = ()=>{
            console.log("Car Socket Connect")
            console.log(JSON.stringify({
                action: 'subscribe_to_car_activity',
                request_id: new Date().getTime()
            }))
            client.send(JSON.stringify({
                action: 'subscribe_to_car_activity',
                request_id: new Date().getTime()
            }))
        }
        client.onmessage = ()=>{
            console.log('::::32')
            setTrigger(prev=> !prev)
        }
        client.onerror = (error) => {
            console.error("WebSocket error: ", error);
        };
    }

    return (
        <div>
            <h3>Cars:</h3>
            {cars.map(car=><CarComponent key={car.id} car={car}/>)}
        </div>
    );
};

export default CarsComponent;