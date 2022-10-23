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
            console.log("hello world");
            const response = await getUsers(7,(position).coords.latitude,(position).coords.longitude);
            console.log("hello world2");
            const code = response.code;
            console.log(code);
            console.log(response);
            let popUpText = "";
            switch (code) {
                // Update
                case 200:
                    popUpText = `Use your ${response["cc_name"]} at ${response["buisiness_name"]}`;
                    break;
                // No update
                case 100:
                    popUpText = "No nearby businesses located.";
                    break;
                // Invalid input    
                case 400:
                    popUpText = "Invalid request data.";
                    break;
                // User doesn't exist
                case 401:
                    popUpText = "Error: User does not exist.";
                    break;
                // **** This is defensive programming; should never hit
                default:
                    popUpText = "An unexpected error has occured.";
                    break;
            }

            
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

async function getUsers(uid: number, lat: number, lon: number): Promise<any> {
    const url = `http://34.85.178.132:5000/api?uid=${uid}&lat=${lat}&lon=${lon}`;
    const response = await fetch(url);
    return await response.json();
}

export default GeolocationButton;