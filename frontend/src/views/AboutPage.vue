<template>
  <section class="text-align-left">
    <h2>A propos</h2>
    <p>
      Vous êtes un des premiers utilisateurs, merci d'être là !
    </p>
    <p>
      Ce site vient tout juste d'être lancé (Mars 2020), et a été développé sur un weekend par quelques passionés.
      Il a pour but d'évoluer en fonctions des retours utilisateurs :)
    </p>

    <br />
    <h3>Contribuer</h3>
    <p>
      On est preneur de tous vos retours !
    </p>
    <p>
      Une page <router-link :to="{ name: 'contribute' }">✍️&nbsp;Contribution</router-link> vous permet de rajouter une question ou un sujet qui vous tiens à coeur. Vous pouvez aussi y laisser vos commentaires et remarques !
    </p>

    <br />
    <h3>Open source</h3>
    <p>
      Le code de l'application, ainsi que les questions, sont visibles sur <a href="https://github.com/raphodn/know-your-planet" target="_blank">la page Github de l'application</a>.
      Si vous avez des commentaires ou des suggestions, vous pouvez y créer des <i>Issues</i> 🙏
    </p>
    <p>
      
    </p>

    <br />
    <h3>Quelques chiffres</h3>
    <p>
      Voir la page <router-link :to="{ name: 'stats' }">📊&nbsp;Statistiques</router-link>.
    </p>

    <br />
    <h3>Nous connaître</h3>
    <p>
      Juste quelques <strong>bénévoles</strong> impliqués et concernés par les questions climat.
    </p>

    <br />
    <h3>Vous souhaitez aller plus loin ?</h3>
    <a href="https://fresqueduclimat.org/" target="_blank">La Fresque du Climat</a><br>
    <a href="https://theshiftproject.org/" target="_blank">The Shift Project</a><br>
    <a href="https://avenirclimatique.org/" target="_blank">Avenir Climatique</a><br>
    <a href="http://adrastia.org/" target="_blank">Adrastia</a><br>
    <a href="https://www.lpo.fr/" target="_blank">La Ligue pour la Protection des Oiseaux (LPO)</a><br>
    <a href="https://www.hautconseilclimat.fr/" target="_blank">Le Haut conseil pour le climat</a><br>
    <a href="https://www.conventioncitoyennepourleclimat.fr/" target="_blank">La Convention Citoyenne pour le climat (CCC)</a><br>

    <br />
    <hr />
    <div class="row actions text-center justify-content-end">
      <div class="col-sm-4">
        <HomeLink />
      </div>
    </div>
  </section>
</template>

<script>
import HomeLink from '../components/HomeLink.vue'

export default {
  name: 'AboutPage',
  components: {
    HomeLink,
  }
}
</script>
