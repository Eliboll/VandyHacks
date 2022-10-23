import { Geolocation, Position } from '@capacitor/geolocation';
import { IonButton, IonLoading, IonToast } from '@ionic/react';
import React, { useState } from 'react';

interface LocationError {
    showError: boolean;
    message?: string;
}

const GeolocationButton: React.FC = () => {
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<LocationError>({ showError: false });
    const [position, setPosition] = useState<Position>();

    const getLocation = async () => {
        setLoading(true);

        try {
            const position = await Geolocation.getCurrentPosition();
            setPosition(position);
            setLoading(false);
            setError({ showError: false });
        } catch (e) {
            if (e instanceof Error) {
                setError({ showError: true, message: e.message });
                setLoading(false);
            }
            else {
                setError({ showError: true, message: (e as Error).message });
                setLoading(false);
            }
        }
    }

    return (
        <>
            <IonLoading
                isOpen={loading}
                onDidDismiss={() => setLoading(false)}
                message={'Getting Location...'}
            />
            <IonToast
                isOpen={error.showError}
                onDidDismiss={() => setError({ message: "", showError: false })}
                message={error.message}
                duration={3000}
            />
            <IonButton color="primary" onClick={getLocation}>{position ? `${position.coords.latitude} ${position.coords.longitude}` : "Get Location"}</IonButton>
        </>
    );
};

export default GeolocationButton;