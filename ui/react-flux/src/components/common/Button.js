import React from "react";
import PropTypes from "prop-types";

function Button(props) {
    let wrapperClase = "save btn btn-default";
    if (props.clicked === true) {
        wrapperClase += " disabled";
    }
    return ( 
        <>
            <button 
                id={props.id}
                name={props.name}
                className={wrapperClase}
                type={props.type}
            >
                {props.label}
            </button>
        </>
    )
}

Button.propTypes = {
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    type: PropTypes.string.isRequired,
    label: PropTypes.string.isRequired,
}

export default Button;