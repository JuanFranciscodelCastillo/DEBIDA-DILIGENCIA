// src/components/Home.js
import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
    return (
        <div className="home">
            <h1>Bienvenido al Sistema de Debida Diligencia</h1>
            <p>Esta aplicación permite realizar y gestionar análisis de riesgo en empresas y clientes.</p>
            <div className="home-links">
                <Link to="/formulario-diligencia" className="home-button">Realizar Nuevo Análisis</Link>
                <Link to="/resultados" className="home-button">Ver Resultados</Link>
            </div>
        </div>
    );
}

export default Home;
