import React from 'react';
import CarFormComponent from "../components/CarFormComponent";
import CarsComponent from "../components/CarsComponent";
import ChatComponent from "../components/ChatComponent";

const CarPage = () => {
    return (
        <div>
            <CarFormComponent/>
            <hr/>
            <CarsComponent/>
            <hr/>
            <ChatComponent/>
        </div>
    );
};

export default CarPage;