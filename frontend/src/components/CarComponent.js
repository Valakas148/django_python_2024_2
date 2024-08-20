import React from 'react';

const CarComponent = ({car}) => {
    const {brand,model,price,year, body_type} = car
    return (
        <div>
            <div>brand: {brand}</div>
            <div>model: {model}</div>
            <div>body_type: {body_type}</div>
            <div>price: {price}</div>
            <div>year: {year}</div>
        </div>
    );
};

export default CarComponent;