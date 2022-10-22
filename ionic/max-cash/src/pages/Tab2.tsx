import React, { useRef } from 'react';
import {
  IonButton,
  useIonToast,
  IonModal,
  IonHeader,
  IonContent,
  IonFab,
  IonFabButton,
  IonToolbar,
  IonTitle,
  IonPage,
  IonList,
  IonItem,
  IonLabel,
  IonIcon,
  IonRadio,
} from '@ionic/react';
import { personCircle, addCircle, happy } from 'ionicons/icons';

import './Tab2.css';

function Tab2() {
  const [present] = useIonToast();

  const presentToast = (position: 'top' | 'middle' | 'bottom') => {
    present({
      message: 'Hello World!',
      duration: 3500,
      position: position
    });
  };

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>MaxCash</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonFab vertical="center" horizontal="center">
        <IonFabButton onClick={() => presentToast('top')}>
          <IonIcon icon={happy}></IonIcon>
        </IonFabButton>
      </IonFab>
    </IonPage>
  );
}

export default Tab2;