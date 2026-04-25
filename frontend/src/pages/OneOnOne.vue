<template>
  <div class="space-y-6 h-full flex flex-col">
    <div class="flex items-center justify-between flex-shrink-0">
      <div>
        <h2 class="text-3xl font-bold text-white tracking-tight">1-on-1 Workspace</h2>
        <p class="text-slate-400 mt-1">Collaborate on agendas and track action items</p>
      </div>
      <button class="bg-white/10 hover:bg-white/20 text-white px-5 py-2.5 rounded-xl font-medium transition-colors border border-white/10 flex items-center gap-2">
        <i data-feather="calendar" class="w-4 h-4"></i> Schedule Meeting
      </button>
    </div>

    <div class="flex-1 grid grid-cols-1 lg:grid-cols-4 gap-6 overflow-hidden">
      
      <!-- Meeting List sidebar -->
      <div class="glass-card flex flex-col overflow-hidden">
        <div class="p-4 border-b border-white/5">
          <h3 class="font-semibold text-slate-200">Upcoming & Past</h3>
        </div>
        <div class="flex-1 overflow-y-auto p-2 space-y-1">
          <div v-if="oneOnOnes.loading" class="text-slate-500 text-sm p-3">Loading...</div>
          <div v-else-if="!oneOnOnes.data || oneOnOnes.data.length === 0" class="text-slate-500 text-sm p-3">No meetings found.</div>
          
          <div v-else v-for="meeting in oneOnOnes.data" :key="meeting.name" 
               @click="selectedMeetingId = meeting.name"
               class="p-3 rounded-lg cursor-pointer transition-colors"
               :class="selectedMeetingId === meeting.name ? 'bg-indigo-500/20 border border-indigo-500/30' : 'hover:bg-white/5'">
            <div class="text-xs font-medium mb-1" :class="isUpcoming(meeting.date) ? 'text-amber-400' : 'text-slate-400'">
              {{ formatDate(meeting.date) }}
            </div>
            <div class="font-semibold" :class="selectedMeetingId === meeting.name ? 'text-white' : 'text-slate-300'">
              {{ meeting.manager }}
            </div>
            <div class="text-xs mt-1 flex items-center gap-1" :class="selectedMeetingId === meeting.name ? 'text-slate-400' : 'text-slate-500'">
               {{ meeting.status }}
            </div>
          </div>
          
        </div>
      </div>

      <!-- Main Workspace -->
      <div class="lg:col-span-3 glass-card flex flex-col overflow-hidden">
        
        <div class="p-6 border-b border-white/5 flex items-center justify-between flex-shrink-0" v-if="selectedMeetingDetails.data">
          <div class="flex items-center gap-4">
            <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-cyan-500 to-blue-500 flex items-center justify-center font-bold text-white">
              {{ getInitials(selectedMeetingDetails.data.manager) }}
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">1-on-1 with {{ selectedMeetingDetails.data.manager }}</h2>
              <p class="text-sm text-indigo-300">{{ formatDate(selectedMeetingDetails.data.date) }}</p>
            </div>
          </div>
          <span class="px-3 py-1 bg-white/5 rounded-full text-xs font-medium border border-white/10" :class="selectedMeetingDetails.data.status === 'Completed' ? 'text-green-400' : 'text-amber-400'">
            {{ selectedMeetingDetails.data.status }}
          </span>
        </div>

        <div class="flex-1 overflow-y-auto p-6 space-y-8" v-if="selectedMeetingDetails.data">
          
          <!-- Shared Agenda -->
          <section>
            <h3 class="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-4 flex items-center gap-2">
              <i data-feather="list" class="w-4 h-4"></i> Shared Agenda
            </h3>
            
            <div class="space-y-3">
              <div v-if="!selectedMeetingDetails.data.agenda_items || selectedMeetingDetails.data.agenda_items.length === 0" class="text-slate-500 text-sm italic">
                No agenda items added yet.
              </div>

              <div v-for="item in selectedMeetingDetails.data.agenda_items" :key="item.name" class="flex items-start gap-3 group">
                <input type="checkbox" :checked="item.discussed" class="mt-1 w-4 h-4 rounded border-slate-600 bg-slate-800 text-indigo-500 focus:ring-indigo-500 focus:ring-offset-slate-900">
                <div class="flex-1">
                  <input type="text" :value="item.topic" class="w-full bg-transparent border-none focus:ring-0 p-0 text-base" :class="item.discussed ? 'text-slate-500 line-through' : 'text-slate-200'">
                </div>
                <span v-if="item.carried_over" class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 text-xs">Carried Over</span>
                <button class="text-slate-500 opacity-0 group-hover:opacity-100 transition-opacity hover:text-red-400"><i data-feather="trash-2" class="w-4 h-4"></i></button>
              </div>

              <div class="flex items-center gap-3 pt-2">
                <i data-feather="plus" class="w-4 h-4 text-slate-500 ml-0.5"></i>
                <input type="text" class="flex-1 bg-transparent border-none text-slate-400 focus:ring-0 p-0 text-sm placeholder-slate-600" placeholder="Add new talking point...">
              </div>
            </div>
          </section>

          <!-- Action Items -->
          <section>
            <h3 class="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-4 flex items-center gap-2">
              <i data-feather="check-square" class="w-4 h-4"></i> Action Items
            </h3>
            
            <div class="text-slate-500 text-sm italic">
              Action items are populated from uncompleted agenda items in previous meetings.
            </div>
          </section>

        </div>
        
        <div v-else class="flex-1 flex items-center justify-center">
           <p class="text-slate-500">Select a meeting from the sidebar.</p>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from 'vue';
import { createListResource, createResource } from 'frappe-ui';
import feather from 'feather-icons';

const oneOnOnes = createListResource({
  doctype: 'PMS 1-on-1',
  fields: ['name', 'manager', 'employee', 'date', 'status'],
  orderBy: 'date desc',
  auto: true
});

const selectedMeetingId = ref(null);

watch(() => oneOnOnes.data, (newData) => {
  if (newData && newData.length > 0 && !selectedMeetingId.value) {
    selectedMeetingId.value = newData[0].name;
  }
});

const selectedMeetingDetails = createResource({
  url: 'frappe.client.get',
  makeParams() {
    return {
      doctype: 'PMS 1-on-1',
      name: selectedMeetingId.value
    };
  },
  auto: true
});

watch(selectedMeetingId, () => {
  if (selectedMeetingId.value) {
    selectedMeetingDetails.fetch();
  }
});

const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
};

const getInitials = (email) => {
  if (!email) return 'U';
  return email.substring(0, 2).toUpperCase();
};

const isUpcoming = (dateString) => {
  if (!dateString) return false;
  return new Date(dateString) > new Date();
};

onMounted(() => {
  feather.replace();
});
</script>
