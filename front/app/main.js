const { createApp } = Vue;

createApp({
  data() {
    return {
      name: '',
      message: '',
      messages: []
    };
  },
  methods: {
    async fetchMsgs() {
      const res = await fetch('/api/messages');
      this.messages = await res.json();
    },
    async send() {
      if (!this.name || !this.message) return;
      await fetch('/api/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: this.name, message: this.message })
      });
      this.name = this.message = '';
      this.fetchMsgs();
    },
    formatDate(iso) {
      return new Date(iso).toLocaleString('fr-FR', {
        day:'2-digit', month:'2-digit', year:'numeric',
        hour:'2-digit', minute:'2-digit'
      });
    }
  },
  mounted() { this.fetchMsgs(); }
}).mount('#app');
