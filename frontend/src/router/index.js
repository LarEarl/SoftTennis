import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import NewsList from "../components/NewsList.vue";
import TournamentList from "../components/TournamentList.vue";
import TournamentDetail from "../components/TournamentDetail.vue";
import PlayerList from "../components/PlayerList.vue";
import NewsDetail from "../components/NewsDetail.vue";
import PlayerDetail from "../components/PlayerDetail.vue";
import MatchCalendar from "../components/MatchCalendar.vue";
import MatchDetail from "../components/MatchDetail.vue";
import FederationContacts from "../components/FederationContacts.vue";
import FederationDocs from "../components/FederationDocs.vue";
import DocumentDetail from "../components/DocumentDetail.vue";
import FederationLeadership from "../components/FederationLeadership.vue";
import LeadershipDetail from "../components/LeadershipDetail.vue";
import FederationTeam from "../components/FederationTeam.vue";
import TeamDetail from "../components/TeamDetail.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/news", component: NewsList },
  { path: "/news/:id", component: NewsDetail, props: true },
  { path: "/tournaments", component: TournamentList },
  { path: "/tournaments/:id", component: TournamentDetail, props: true },
  { path: "/players", component: PlayerList },
  { path: "/players/:id", component: PlayerDetail, props: true },
  { path: "/matches", component: MatchCalendar },
  { path: "/matches/:id", component: MatchDetail, props: true },
  { path: "/federation/contacts", component: FederationContacts },
  { path: "/federation/docs", component: FederationDocs },
  { path: "/federation/docs/:id", component: DocumentDetail },
  { path: "/federation/leadership", component: FederationLeadership },
  { path: "/federation/leadership/:id", component: LeadershipDetail },
  { path: "/federation/team", component: FederationTeam },
  { path: "/federation/team/:id", component: TeamDetail },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
