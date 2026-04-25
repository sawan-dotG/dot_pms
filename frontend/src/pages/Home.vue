<template>
  <div class="space-y-8">
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-3xl font-bold text-white tracking-tight">Welcome back, Sawan 👋</h2>
        <p class="text-slate-400 mt-1">Here's what's happening with your performance and growth.</p>
      </div>
      <div class="text-right">
        <p class="text-sm font-medium text-slate-400">Current Cycle</p>
        <p class="text-lg font-bold text-indigo-400">Q2 2026 Appraisal</p>
      </div>
    </div>

    <!-- Quick Stats Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <!-- OKR Stat -->
      <div class="glass-card p-6 border-l-4 border-indigo-500 relative overflow-hidden group">
        <div class="absolute top-0 right-0 -mt-4 -mr-4 w-24 h-24 bg-indigo-500/20 rounded-full blur-xl group-hover:bg-indigo-500/30 transition-colors"></div>
        <div class="flex items-start justify-between relative z-10">
          <div>
            <p class="text-sm font-medium text-slate-400">OKR Progress</p>
            <h3 class="text-3xl font-bold text-white mt-1">{{ avgProgress }}%</h3>
          </div>
          <div class="w-10 h-10 rounded-xl bg-indigo-500/20 flex items-center justify-center text-indigo-400">
            <i data-feather="target" class="w-5 h-5"></i>
          </div>
        </div>
        <div class="mt-4 flex items-center gap-2 text-sm">
          <span class="text-emerald-400 flex items-center font-medium"><i data-feather="trending-up" class="w-3 h-3 mr-1"></i> Active</span>
          <span class="text-slate-500">Based on {{ objectives.data?.length || 0 }} objectives</span>
        </div>
      </div>

      <!-- Feedback Stat -->
      <div class="glass-card p-6 border-l-4 border-emerald-500 relative overflow-hidden group">
        <div class="absolute top-0 right-0 -mt-4 -mr-4 w-24 h-24 bg-emerald-500/20 rounded-full blur-xl group-hover:bg-emerald-500/30 transition-colors"></div>
        <div class="flex items-start justify-between relative z-10">
          <div>
            <p class="text-sm font-medium text-slate-400">Recent Feedback</p>
            <h3 class="text-3xl font-bold text-white mt-1">{{ feedbackCount }}</h3>
          </div>
          <div class="w-10 h-10 rounded-xl bg-emerald-500/20 flex items-center justify-center text-emerald-400">
            <i data-feather="award" class="w-5 h-5"></i>
          </div>
        </div>
        <div class="mt-4 flex items-center gap-2 text-sm">
          <span class="text-emerald-400 flex items-center font-medium"><i data-feather="trending-up" class="w-3 h-3 mr-1"></i> {{ recentFeedback.length > 0 ? 'Active feed' : 'No new feed' }}</span>
          <span class="text-slate-500">Total recorded</span>
        </div>
      </div>

      <!-- 1on1 Stat -->
      <div class="glass-card p-6 border-l-4 border-amber-500 relative overflow-hidden group">
        <div class="absolute top-0 right-0 -mt-4 -mr-4 w-24 h-24 bg-amber-500/20 rounded-full blur-xl group-hover:bg-amber-500/30 transition-colors"></div>
        <div class="flex items-start justify-between relative z-10">
          <div>
            <p class="text-sm font-medium text-slate-400">Next 1-on-1</p>
            <h3 class="text-xl font-bold text-white mt-1">{{ nextMeeting }}</h3>
          </div>
          <div class="w-10 h-10 rounded-xl bg-amber-500/20 flex items-center justify-center text-amber-400">
            <i data-feather="calendar" class="w-5 h-5"></i>
          </div>
        </div>
        <div class="mt-4 flex items-center gap-2 text-sm">
          <span class="text-amber-400 flex items-center font-medium" v-if="oneOnOnes.data && oneOnOnes.data.length > 0"><i data-feather="alert-circle" class="w-3 h-3 mr-1"></i> Action needed</span>
          <span class="text-slate-500" v-if="oneOnOnes.data && oneOnOnes.data.length > 0">1 upcoming</span>
        </div>
      </div>

    </div>

    <!-- Main Content Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      
      <!-- Action Items Widget -->
      <div class="glass-card p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-bold text-white">Pending Action Items</h3>
          <router-link to="/1on1" class="text-sm font-medium text-indigo-400 hover:text-indigo-300">View All</router-link>
        </div>
        
        <div class="space-y-4">
          <div class="flex items-start gap-3 group">
            <input type="checkbox" class="mt-1 w-4 h-4 rounded border-slate-600 bg-slate-800 text-indigo-500 focus:ring-indigo-500 focus:ring-offset-slate-900 cursor-pointer">
            <div class="flex-1">
              <p class="text-sm font-medium text-slate-200 group-hover:text-white transition-colors">Complete Frappe Integration Doc</p>
              <p class="text-xs text-slate-500 mt-1">From 1-on-1 on Oct 12</p>
            </div>
            <span class="px-2 py-0.5 rounded bg-red-500/10 text-red-400 text-xs font-medium border border-red-500/20">Overdue</span>
          </div>

          <div class="flex items-start gap-3 group">
            <input type="checkbox" class="mt-1 w-4 h-4 rounded border-slate-600 bg-slate-800 text-indigo-500 focus:ring-indigo-500 focus:ring-offset-slate-900 cursor-pointer">
            <div class="flex-1">
              <p class="text-sm font-medium text-slate-200 group-hover:text-white transition-colors">Update Q2 OKRs in dotG</p>
              <p class="text-xs text-slate-500 mt-1">From 1-on-1 on Oct 19</p>
            </div>
            <span class="px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 text-xs font-medium border border-amber-500/20">Due Today</span>
          </div>
        </div>
      </div>

      <!-- Recent Feedback Widget -->
      <div class="glass-card p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-bold text-white">Recent Feedback</h3>
          <router-link to="/feedback" class="text-sm font-medium text-indigo-400 hover:text-indigo-300">Give Feedback</router-link>
        </div>

        <div class="space-y-4">
          <div v-if="feedback.loading" class="text-slate-500 text-sm">Loading...</div>
          <div v-else-if="recentFeedback.length === 0" class="text-slate-500 text-sm">No recent feedback.</div>
          <div v-else v-for="item in recentFeedback" :key="item.name" class="flex gap-4 p-3 rounded-xl hover:bg-white/5 transition-colors cursor-pointer">
            <div class="w-10 h-10 rounded-full bg-gradient-to-br from-green-400 to-emerald-600 flex-shrink-0 flex items-center justify-center font-bold text-white text-sm">
              {{ getInitials(item.from_user) }}
            </div>
            <div class="flex-1">
              <div class="flex justify-between items-start">
                <p class="text-sm font-medium text-white">{{ item.from_user }}</p>
                <span class="text-xs text-slate-500">{{ timeAgo(item.creation) }}</span>
              </div>
              <p class="text-sm text-slate-300 mt-1 line-clamp-2">{{ item.content }}</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from 'vue';
import { createListResource } from 'frappe-ui';
import feather from 'feather-icons';

// Fetch OKRs
const objectives = createListResource({
  doctype: 'PMS Objective',
  fields: ['name', 'title', 'progress'],
  auto: true
});

const avgProgress = computed(() => {
  if (!objectives.data || objectives.data.length === 0) return 68; // fallback to dummy for visual if no data
  const sum = objectives.data.reduce((acc, obj) => acc + (obj.progress || 0), 0);
  return Math.round(sum / objectives.data.length);
});

// Fetch Feedback
const feedback = createListResource({
  doctype: 'PMS Feedback',
  fields: ['name', 'from_user', 'to_user', 'sentiment', 'content', 'creation'],
  orderBy: 'creation desc',
  limit: 5,
  auto: true
});

const recentFeedback = computed(() => feedback.data || []);
const feedbackCount = computed(() => feedback.data ? feedback.data.length : 12);

// Fetch 1-on-1s
const oneOnOnes = createListResource({
  doctype: 'PMS 1-on-1',
  fields: ['name', 'manager', 'employee', 'date', 'status'],
  orderBy: 'date asc',
  filters: { status: ['!=', 'Completed'] },
  limit: 1,
  auto: true
});

const nextMeeting = computed(() => {
  if (oneOnOnes.data && oneOnOnes.data.length > 0) {
    const meetingDate = new Date(oneOnOnes.data[0].date);
    return meetingDate.toLocaleDateString() + ' ' + meetingDate.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
  }
  return "No upcoming meetings";
});

// Helper to get initials
const getInitials = (email) => {
  if (!email) return 'U';
  return email.substring(0, 2).toUpperCase();
};

const timeAgo = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  const now = new Date();
  const diffHours = Math.round((now - date) / (1000 * 60 * 60));
  if (diffHours < 24) return `${diffHours}h ago`;
  const diffDays = Math.round(diffHours / 24);
  return `${diffDays}d ago`;
};

onMounted(() => {
  feather.replace();
});
</script>
