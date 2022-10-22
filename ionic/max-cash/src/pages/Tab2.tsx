import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import ExploreContainer from '../components/ExploreContainer';
import './Tab2.css';

const Tab2: React.FC = () => {
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>MaxCash Title</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">MaxCash Toolbar</IonTitle>
          </IonToolbar>
        </IonHeader>
        <ExploreContainer name="MaxCash page" />
      </IonContent>
    </IonPage>
  );
};

export default Tab2;
