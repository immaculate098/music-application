import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Artists = () => {
    const [artists, setArtists] = useState([]);

    useEffect(() => {
        axios.get('/api/artists/')
            .then(response => setArtists(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Artists</h1>
            <ul>
                {artists.map(artist => (
                    <li key={artist.id}>{artist.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default Artists;
