import React from 'react';
import {useForm} from "react-hook-form";
import {carService} from "../services/carService";

const CarFormComponent = () => {
    const {register, handleSubmit, reset} = useForm()

    const save = async (car)=>{
        // car.price = parseInt(car.price, 10);
        // car.year = parseInt(car.year, 10);
        await carService.create(car);
        reset()
    }

    return (
        <form onSubmit={handleSubmit(save)}>
            <h1>CarForm</h1>
            <input type="text" placeholder={'brand'} {...register('brand')}/>
            <input type="text" placeholder={'model'} {...register('model')}/>
            <input type="text" placeholder={'price'} {...register('price')}/>
            <input type="text" placeholder={'year'} {...register('year')}/>
            <input type="text" placeholder={'body_type'} {...register('body_type')}/>
            <button>Save</button>
        </form>
    );
};

export default CarFormComponent;