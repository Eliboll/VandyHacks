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
import { personCircle, addCircle } from 'ionicons/icons';

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
              <h1>Dialog header</h1>
          
              <IonList lines="none">
                <IonItem button={true} detail={false} onClick={dismiss}>
                  <IonIcon icon={personCircle}></IonIcon>
                  <IonLabel>Credit Card 1</IonLabel>
                  <IonRadio slot="start" value="one" />
                </IonItem>
                <IonItem button={true} detail={false} onClick={dismiss}>
                  <IonIcon icon={personCircle}></IonIcon>
                  <IonLabel>Item 2</IonLabel>
                </IonItem>
                <IonItem button={true} detail={false} onClick={dismiss}>
                  <IonIcon icon={personCircle}></IonIcon>
                  <IonLabel>Item 3</IonLabel>
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