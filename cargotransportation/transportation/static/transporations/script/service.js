let checkbox = document.querySelector(`#checkbox`);
let type_cargo = document.querySelector(`#type_cargo`);
let cargo_weight = document.querySelector(`#cargo_weight`);
let type_transportation = document.querySelector(`#type_transportation`);
let route_length = document.querySelector(`#route_length`);
let price = document.querySelector(`#price`);
let btn_service = document.querySelector(`#btn_service`);

let route_length_val = 0;
let cargo_weight_val = 0;
let checkbox_val = 0;
let type_cargo_val;
let type_transportation_val;

let summa = 0;

btn_service.addEventListener(`click`, () => {
    cargo_weight_val = 13 * cargo_weight.value;
    route_length_val= 17 * route_length.value;

    if (checkbox.checked) { 
        checkbox_val = 5000
    }
    else checkbox_val = 0
    
    switch (type_cargo.value) {
        case `Навалочной`:
            type_cargo_val = 10000
            break;
        case `Насыпной`:
            type_cargo_val = 3000
            break;
        case `Штучный`:
            type_cargo_val = 15000
            break;
        case `Наливной`:
            type_cargo_val = 20000
            break;
        case ``:
            type_cargo_val = 0
            break;
        default:
            type_cargo_val = 5000
            break;
    }
    
    switch (type_transportation.value) {
        case `Автомобильный`:
            type_transportation_val = 10000
            break;
        case `Железнодорожный`:
            type_transportation_val = 5000
            break;
        case `Воздушный`:
            type_transportation_val = 25000
            break;
        case `Морской`:
            type_transportation_val = 15000
            break;
        case ``:
            type_transportation_val = 0
            break;
        default:
            type_transportation_val = 1000
            break;
    }

    summa = checkbox_val + type_cargo_val + cargo_weight_val + type_transportation_val + route_length_val

    price.innerHTML = `${summa}р.`
});
