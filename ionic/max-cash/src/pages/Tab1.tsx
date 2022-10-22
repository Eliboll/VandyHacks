import React, { useRef } from 'react';
import {
  IonButton,
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
import { personCircle, addCircle, card } from 'ionicons/icons';

import './Tab1.css';

function Tab1() {
  const modal = useRef<HTMLIonModalElement>(null);

  function dismiss() {
    modal.current?.dismiss();
  }

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>My Cards</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent class="ion-padding">
        <IonFab vertical="bottom" horizontal="center" slot="fixed">
          <IonFabButton id="open-custom-dialog">
            <IonIcon icon={addCircle}></IonIcon>
          </IonFabButton>
          <IonModal id="example-modal" ref={modal} trigger="open-custom-dialog">
            <div className="wrapper">
              <h1>Add a card</h1>
          
              <IonList lines="none">
                <IonItem button={true} detail={false} onClick={dismiss}>
                  <IonIcon icon={card}></IonIcon>
                  <IonLabel id='1'>&nbsp;Credit Card 1</IonLabel>
                </IonItem>
                <IonItem button={true} detail={false} onClick={dismiss}>
                  <IonIcon icon={card}></IonIcon>
                  <IonLabel id='2'>&nbsp;Credit Card 2</IonLabel>
                </IonItem>
                <IonItem button={true} detail={false} onClick={dismiss}>
                  <IonIcon icon={card}></IonIcon>
                  <IonLabel id='3'>&nbsp;Credit Card 3</IonLabel>
                </IonItem>
              </IonList>
            </div>
          </IonModal>
        </IonFab>
      </IonContent>
    </IonPage>
  );
}

export default Tab1;